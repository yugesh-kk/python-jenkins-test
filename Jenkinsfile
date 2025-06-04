pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                bat 'python system_info.py'
            }
        }

        stage('Archive Log') {
            steps {
                archiveArtifacts artifacts: 'output_*.log', onlyIfSuccessful: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed. Check output.log for system info.'
        }
    }
}
