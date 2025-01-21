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
                sh 'python -m unittest discover -s tests'
            }
        }
    }
}
