from flask import Flask, render_template, request, jsonify
import os
import importlib.util
import glob

app = Flask(__name__)

class PluginManager:
    def __init__(self):
        self.plugins = {}
        self.operations = {}
        self.plugins_dir = 'plugins'
        self.load_plugins()
    
    def load_plugins(self):
        """Загрузка всех плагинов из папки plugins"""
        print("\n=== ЗАГРУЗКА ПЛАГИНОВ ===")
        self.plugins.clear()
        self.operations.clear()
        
        # Проверяем существование папки
        if not os.path.exists(self.plugins_dir):
            print(f"❌ Папка {self.plugins_dir} не найдена!")
            os.makedirs(self.plugins_dir)
            print(f"✅ Создана папка {self.plugins_dir}")
            return
        
        plugin_files = glob.glob(os.path.join(self.plugins_dir, 'plugin_*.py'))
        print(f"📁 Найдено файлов плагинов: {len(plugin_files)}")
        
        for plugin_file in plugin_files:
            print(f"\n🔌 Загрузка: {plugin_file}")
            try:
                module_name = os.path.basename(plugin_file)[:-3]
                print(f"   Имя модуля: {module_name}")
                
                spec = importlib.util.spec_from_file_location(module_name, plugin_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                if hasattr(module, 'register'):
                    plugin = module.register()
                    print(f"   ✅ Плагин зарегистрирован: {plugin.get('name', 'Unknown')}")
                    print(f"   Операции: {plugin['operations']}")
                    
                    self.plugins[module_name] = plugin
                    
                    for op in plugin['operations']:
                        self.operations[op] = {
                            'plugin': module_name,
                            'calculate': plugin['calculate']
                        }
                else:
                    print(f"   ⚠️ В модуле нет функции register()")
                    
            except Exception as e:
                print(f"   ❌ Ошибка: {e}")
                import traceback
                traceback.print_exc()
        
        print(f"\n=== ВСЕГО ОПЕРАЦИЙ: {len(self.operations)} ===")
        print(f"Список: {list(self.operations.keys())}\n")
    
    def get_operations(self):
        return list(self.operations.keys())
    
    def calculate(self, operation, a, b):
        if operation not in self.operations:
            raise Exception(f"Операция '{operation}' не найдена")
        plugin_info = self.operations[operation]
        return plugin_info['calculate'](operation, a, b)

# Инициализация
plugin_manager = PluginManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/operations')
def get_operations():
    print("📡 Запрос /api/operations")
    ops = plugin_manager.get_operations()
    print(f"   Возвращаю: {ops}")
    return jsonify({
        'success': True,
        'operations': ops
    })

@app.route('/api/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        print(f"📡 Запрос /api/calculate: {data}")
        
        op = data.get('op')
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        
        result = plugin_manager.calculate(op, a, b)
        
        return jsonify({
            'success': True,
            'result': result
        })
    except Exception as e:
        print(f"❌ Ошибка вычисления: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    print("🚀 ЗАПУСК СЕРВЕРА...")
    print("Откройте http://localhost:5000\n")
app.run(debug=True, port=5000)