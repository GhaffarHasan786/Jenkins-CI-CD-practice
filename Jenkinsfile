pipeline {
    agent any
    stages {
        stage('Code pull') {
            steps {
                echo 'Step 1: Checking files in workspace...'
                sh 'ls -la'
            }
        }
        stage('Run python script') {
            steps {
                echo 'Step 2: Running Python script...'
                sh 'python3 freestyle_jobs/app.py'
            }
        
            }
        }
    }
