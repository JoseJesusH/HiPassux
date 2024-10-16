pipeline {
    agent any
    tools {
        maven 'Maven' // Make sure Maven is configured in Jenkins
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/JoseJesusH/HiPassux.git'
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
            junit 'target/surefire-reports/*.xml'
        }
    }
}

