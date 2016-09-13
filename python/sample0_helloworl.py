import qarnot
conn = qarnot.connection.Connection({'client_auth': 'xxxx-mytoken-xxxx'})
task = conn.create_task('sample0_helloworld', 'docker-batch', 1)
task.constants['DOCKER_CMD'] = 'echo hello world!'
task.run()
print(task.stdout())
