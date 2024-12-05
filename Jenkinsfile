pipeline {
    agent any

    stages {
        stage('Clonar Repositório') {
            steps {
                git branch: 'main', url: 'https://github.com/ggoncalves17/Aplicacao-Django-LP-Lab07.git'
            }
        }
        stage('Configurar Ambiente') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Migrações da Base de Dados') {
            steps {
                bat 'python manage.py migrate --noinput'
            }
        }
        stage('Executar Testes') {
            steps {
                bat '''
                    python -m pytest --junitxml=test-reports/results.xml --cov=. --cov-report=xml
                '''
            }
        }
        stage('Gerar Relatórios de Cobertura') {
            steps {
                bat '''
                    coverage html -d htmlcov
                '''
            }
        }
    }

    post {
        always {
            junit 'test-reports/results.xml'
            publishCoverage adapters: [coberturaAdapter(path: '/coverage.xml')], sourceFileResolver: sourceFiles('NEVER_STORE')
            archiveArtifacts artifacts: 'htmlcov/', fingerprint: true
        }
        failure {
            echo 'Build falhou!'
        }
    }
}