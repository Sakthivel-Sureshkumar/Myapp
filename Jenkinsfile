pipeline {
  agent any

  environment {
    APP_NAME = "flaskapp"
    IMAGE    = "flaskapp"
    PORT     = "5000"
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Docker Build') {
      steps {
        sh '''
          set -e
          echo "Building image: ${IMAGE}:${BUILD_NUMBER}"
          docker build -t ${IMAGE}:${BUILD_NUMBER} .
        '''
      }
    }

    stage('Run Container') {
      steps {
        sh '''
          set -e
          docker rm -f ${APP_NAME} || true
          docker run -d --name ${APP_NAME} -p ${PORT}:${PORT} ${IMAGE}:${BUILD_NUMBER}
          docker ps
        '''
      }
    }
  }
}