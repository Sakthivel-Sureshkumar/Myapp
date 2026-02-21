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
          echo "Building Docker image..."
          docker build -t ${IMAGE}:${BUILD_NUMBER} .
        '''
      }
    }

    stage('Stop Old Container') {
      steps {
        sh '''
          docker rm -f ${APP_NAME} || true
        '''
      }
    }

    stage('Run Container') {
      steps {
        sh '''
          docker run -d --name ${APP_NAME} -p ${PORT}:${PORT} ${IMAGE}:${BUILD_NUMBER}
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