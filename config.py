from environ import Env

env = Env()
Env.read_env('.env')


BACKEND_URL = env("BACKEND_URL")
