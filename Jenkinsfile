pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the Python project...'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests'
            }
        }
    }
}
