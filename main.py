'''
Created on Nov 6, 2022

@author: Admin
'''
# main.py
import demopackage
# main.py
 
# main.py
import demopackage.modules as modules
# main.py
# main.py
from demopackage.packagechild.childmodule import *
from demopackage.packagechild.rectangle import Rectangle
from db_firebase.load_db  import *
from core.ngrok_join_system  import *
from core.build_main_dashboard  import *
from core.api_input  import *


from core.get_layout_data  import *

app = Flask(__name__) #app name
run_with_ngrok(app)
join_system()
init_firebase()

@app.route('/draft/core/get_main_dashboard_app', methods=['POST'])
def api_input_get_main_dashboard_app (): 
    return api_input_get_main_dashboard_app_post(request)
@app.route('/draft/core/get_layout_data', methods=['POST'])
def draft_core_get_layout_data (): 
    return core_get_layout_data_post(request)

@app.route('/api/input/', methods=['POST'])
def api_input ():
   return api_input_post(request)
    
if __name__ == "__main__":
    app.run()
