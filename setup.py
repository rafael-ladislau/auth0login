from setuptools import setup

setup(name='auth0login',
      version='0.1',
      description='Auth0 Authentication Backend for Social Django',
      url='http://github.com/rafael-ladislau/auth0login',
      author='Rafael Ladislau',
      author_email='rafa.ladis@gmail.com',
      license='MIT',
      packages=['auth0login'],
      install_requires=[
            'six',
            'django',
            'social-auth-app-django',
            'python-jose',
            'python-dotenv',
      ],
      zip_safe=False)
