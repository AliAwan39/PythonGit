pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/AliAwan39/PythonGit.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Lint Code') {
            steps {
                sh 'venv/bin/pip install flake8'
                sh 'venv/bin/flake8 . || true'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'venv/bin/pytest'
            }
        }

        stage('Build') {
            steps {
                sh '''
                mkdir -p build
                cp hello.py build/
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'build/*', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'pipeline finished...'
        }
        success {
            echo 'pipeline succeeded...'
        }
        failure {
            echo 'pipeline failed...'
        }
    }
}