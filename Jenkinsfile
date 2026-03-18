pipeline {
    agent any

    environment {
        APP_NAME = "sample-python-app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/sachinhdin-netigen/Pythoncode.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage ('Run App') {
            steps {
                sh 'python3 main.py'
            }
        }
                stage('Build') {
            steps {
                sh 'echo "Building application..."'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying application..."'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Build successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
