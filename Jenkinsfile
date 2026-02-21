pipeline {
  agent any

  environment {
    APP_NAME = "flaskapp"
    IMAGE    = "flaskapp"
    PORT     = "5000"
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        sh '''
          echo "Cleaning old docker images..."
          docker system prune -af || true

          echo "Building fresh image..."
          docker build -t ${IMAGE}:latest .
        '''
      }
    }

    stage('Deploy Container') {
      steps {
        sh '''
          docker rm -f ${APP_NAME} || true
          docker run -d --name ${APP_NAME} -p ${PORT}:${PORT} ${IMAGE}:latest
        '''
      }
    }

    stage('Verify') {
      steps {
        sh 'docker ps'
      }
    }
  }
}