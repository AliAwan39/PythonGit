pipeline{
    agent any
    
    triggers{
        githubPush()
    }

    stages{
        stage('Checkout Code'){
            steps{
                echo 'Checking out the code...'
                git "https://github.com/AliAwan39/PythonGit.git"
            }
        }
        stage('setup environment'){
            steps{
                echo 'setting up environment...'
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                sh 'venv/bin/pip install -r requirements.txt'
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
                sh 'echo "Building project..."'
                sh 'mkdir -p build'
                sh 'cp hello.py build/'
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