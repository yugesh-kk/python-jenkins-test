pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/yugesh-kk/python-jenkins-test.git'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 system_info.py'
            }
        }

        stage('Archive Log') {
            steps {
                archiveArtifacts artifacts: 'output.log', onlyIfSuccessful: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed. Check output.log for system info.'
        }
    }
}
