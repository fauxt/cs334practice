pipeline {
  agent {
    docker {
      image 'python:3.8'
    }
  }
  stages {
    stage('Create Virtual Environment') {
      steps {
        sh '''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install -r requirements.txt
          pip install .
        '''
      }
    }

    stage('Unit Tests') {
      steps {
        sh '''
          . .venv/bin/activate
          pytest --cov=cs334demo --cov-fail-under=90
        '''
      }
    }
    stage('Static Analysis') {
      steps {
        sh '''
          . .venv/bin/activate
          pylint src/cs334demo/*.py tests/*.py
        '''
      }
    }
  }
}
