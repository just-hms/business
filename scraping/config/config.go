package config

import (
	"github.com/ilyakaznacheev/cleanenv"
)

type (
	Config struct {
		NewsApiKey string `env:"NEWS_API_KEY"`
	}
)

func New() (*Config, error) {
	cfg := &Config{}

	err := cleanenv.ReadConfig(".env", cfg)
	if err != nil {
		return nil, err
	}

	return cfg, nil
}
