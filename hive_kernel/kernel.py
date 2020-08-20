import pandas as pd
import sqlalchemy as sa
from ipykernel.kernelbase import Kernel


__version__ = '0.3.0'

class HiveKernel(Kernel):
    implementation = 'hive_kernel'
    implementation_version = __version__
    language = 'sql'
    language_version = 'latest'
    language_info = {'name': 'sql',
                     'mimetype': 'text/x-sh',
                     'file_extension': '.sql'}
    banner = 'hive kernel'

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.engine = False
        
    def output_help(self):
        msg = ["Hive kernel help document", "name: 'hive_kernel'",
        "version: '0.3.0'",
        "description: 'A hive kernel for Jupyter.'",
        "homepage: https://github.com/Hourout/hive_kernel",
        "author: 'JinQing Lee'",
        "author_email: 'hourout@163.com'",
        "Step1: you should set you hive ip and port.",
        "example",
        "```",
        "hive://127.0.0.1:10000;",
        "```",
        "Step2: write your hive sql",
        "example",
        "```",
        "select date_sub(current_date, 1) dd;",
        "```",
        "Tips:",
        "Every time you write a complete sql, it is best to add ';' at the end."]
        for i in msg:
             self.output(i)
    
    def output_fix(self, output):
        try:
            a = output
            k = a[a.find('statusCode='):a.find(', infoMessages')].replace('=', ':')+'\n'
            k += a[a.find('sqlState'):a.find( 'errorCode')].replace('=',':').rstrip()+'\n'
            k += a[a.find( 'errorCode'):a.find('errorMessage')].replace('=',':')+'\n'
            k += 'infoMessages:\n'
            for i in a[a.find('infoMessages')+13:a.find('sqlState')].split(','):
                k = k+i+'\n'
            k += 'errorMessage:\n'
            k += a[a.find('errorMessage')+13:a.find('operationHandle')].replace('=',':')[:-3]
            k = k.replace("'", '').replace('"', '').replace(",", '')
        except:
            k = output
        return k
                
    def output(self, output):
        if not self.silent:
            display_content = {'source': 'kernel',
                               'data': {'text/html': output},
                               'metadata': {}}
            self.send_response(self.iopub_socket, 'display_data', display_content)
    
    def ok(self):
        return {'status':'ok', 'execution_count':self.execution_count, 'payload':[], 'user_expressions':{}}

    def err(self, msg):
        return {'status':'error',
                'error':msg,
                'traceback':[msg],
                'execution_count':self.execution_count,
                'payload':[],
                'user_expressions':{}}

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        self.silent = silent
        output = ''
        if not code.strip():
            return self.ok()
        sql = code.rstrip()+('' if code.rstrip().endswith(";") else ';')
        try:
            for v in sql.split(";"):
                v = v.rstrip()
                l = v.lower()
                if len(l)>0:
                    if l.startswith('hive://'):
                        if l.count('@')>1:
                            self.output("Connection failed, The hive address cannot have two '@'.")
                        else:
                            self.engine = sa.create_engine(f'{l}')
                    elif l.startswith('set '):
                        pd.io.sql.execute(l, con=self.engine)
                    elif l.startswith('create database '):
                        pd.io.sql.execute(l, con=self.engine)
                    elif l.startswith('create schema '):
                        pd.io.sql.execute(l, con=self.engine)
                    elif l.startswith('drop database '):
                        pd.io.sql.execute(l, con=self.engine)
                    elif l.startswith('drop schema '):
                        pd.io.sql.execute(l, con=self.engine)
                    elif l.startswith('drop table '):
                        pd.io.sql.execute(l, con=self.engine)
                    elif l.startswith('alter table '):
                        pd.io.sql.execute(l, con=self.engine)
                    elif l.startswith('help'):
                        self.output_help()
                    else:
                        if self.engine:
                            if l.startswith('select '):
                                output = pd.read_sql(l+' limit 1000', self.engine).to_html()
                            else:
                                output = pd.read_sql(l, self.engine).to_html()
                        else:
                            output = 'Unable to connect to Hive server. Check that the server is running.'
            self.output(output)
            return self.ok()
        except Exception as msg:
            self.output(self.output_fix(str(msg)))
            return self.err('Error executing code ' + sql)
