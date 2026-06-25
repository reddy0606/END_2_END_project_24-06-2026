pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/reddy0606/END_2_END_project_24-06-2026.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Create Reports Folder') {
            steps {
                sh 'mkdir -p reports'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --html=reports/report.html'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
            }
        }
    }
}
