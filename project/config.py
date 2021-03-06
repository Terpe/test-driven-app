# services/users/project/config.py

class BaseConfig:
    """Base configuration"""
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass

class TestingConfig(BaseConfig):
    """Testing configuration"""
    pass

class ProductionConfig(BaseConfig):
    """Producition configuration"""
    pass

