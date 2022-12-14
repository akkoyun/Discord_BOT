# Import Libraries
from pydantic import BaseSettings

# Define Setting
class Settings(BaseSettings):

	DISCORD_TOKEN: str
	DISCORD_GUILD: str

	class Config:
		env_file = "config/.env"

# Set Setting
APP_Settings = Settings()
