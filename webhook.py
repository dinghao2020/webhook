def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    os.chdir('/tmp/git/test')
    os.system('test -d /tmp/git/test/test_wehook || git clone git@git.cimyun.com:sa/test_wehook.git')
    os.chdir('/tmp/git/test/test_wehook')
    #os.system('git add .')
    #os.system('git commit -m "merge"')
    os.system('git pull ')
    print('git pull finish')
    return [b'<h1>Hello, webhook!</h1>']
