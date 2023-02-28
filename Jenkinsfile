pipeline {
    environment {
        PATH = '~/drivers'
    }
    agent{
        docker{
        args '-e "HOME=/Users/anastasiiamonakhova/.jenkins/workspace/opencart-tests"'
        image 'python:3' }
    }
  stages {
         stage('Get Code') {
            steps {
                 sh 'rm -r *'
                 sh 'git clone https://github.com/an-mengqi/seleium-tests-with-jenkins.git'
            }
         }
    stage('build') {
      steps {
        sh 'ls ~'
        sh 'pip install --user -r seleium-tests-with-jenkins/requirements.txt'
        echo "PATH is: ${env.PATH}"
      }
    }
    stage('test') {
      steps {
        sh 'mkdir seleium-tests-with-jenkins/logs'
        sh 'python -m pytest seleium-tests-with-jenkins/tests/test_admin.py --url=http://192.168.0.15:8081/admin'
      }
    }
  }
}
