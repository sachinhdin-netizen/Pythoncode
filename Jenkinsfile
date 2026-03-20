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
                    pip3 install -r requirements.txt || true
                '''
            }
        }

        stage('Start Web Server') {
            steps {
                echo "Starting Hello World server..."
                sh '''
                    nohup python3 -u main.py > server.log 2>&1 &
                    echo $! > server.pid
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running unit tests..."
                sh 'python3 -m unittest discover -s tests -p "test_*.py" || true'
            }
        }

        stage('Build') {
            steps {
                echo "Building application..."
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
            }
        }
    }

    post {
        always {
            echo 'Cleaning up server process...'
            sh '''
                if [ -f server.pid ]; then
                    kill $(cat server.pid) || true
                    rm -f server.pid
                fi
            '''
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
