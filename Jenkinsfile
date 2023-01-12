@Library('sharedlibrary@1') _
envVars = envVars()

pipeline {
    stages {
        stage('Example') {
            steps {
                script {
                    printVar("newrelicURL", envVars["newrelicURL"])
                    newrelicCheck(envVars)
                }
            }
        }
        stage('Error handling') {
            steps {
                script {
                    try {
                        raise ValueError("this is a test error")
                    } catch (error) {
                        handleError(error)
                    }
                }
            }
        }
    }
}
