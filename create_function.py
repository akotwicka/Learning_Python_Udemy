from datetime import datetime

def create_function(span):
    dict = {'m': 60, 'h': 3600, 'd': 86400}
    sec = dict[span]
    source = '''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]    
'''.format(sec)
    exec(source, globals())
    return f

f_minutes = create_function('m')
f_hours = create_function('h')
f_days = create_function('d')

start = datetime(2019, 1, 1, 0, 0, 0)
end  = datetime.now()

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))
