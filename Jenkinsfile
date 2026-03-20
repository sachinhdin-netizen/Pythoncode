pipeline {
    agent any

    environment {
        APP_NAME = "sample-python-app"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/sachinhdin-netizen/Pythoncode.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 --version
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                echo "Running main.py..."
                sh 'python3 main.py'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running unit tests..."
                // Option 1: Using unittest
                sh 'python3 -m unittest discover -s tests -p "test_*.py"'

                // Option 2 (better reporting): Uncomment below if you install pytest
                // sh 'pytest --junitxml=results.xml tests/'
                // junit 'results.xml'
            }
        }

        stage('Build') {
            steps {
                echo "Building application..."
                // Add packaging steps here if needed
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
                // Add real deployment steps here
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
