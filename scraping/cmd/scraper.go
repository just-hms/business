package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"net/url"
	"os"

	"github.com/joho/godotenv"
)

func main() {
	// Load environment variables from .env file
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}

	// Get the API key from the environment variables
	apiKey := os.Getenv("NEWS_API_KEY")

	// Make the API request
	u := "https://newsapi.org/v2/top-headlines"
	params := url.Values{
		"country": {"it"},
		"apiKey":  {apiKey},
	}

	resp, err := http.Get(u + "?" + params.Encode())
	if err != nil {
		log.Fatal("Error making the request:", err)
	}
	defer resp.Body.Close()

	// Check if the request was successful
	if resp.StatusCode != http.StatusOK {
		log.Fatal("Error:", resp.Status)
	}
	var data map[string]interface{}
	if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
		log.Fatal("Error decoding response:", err)
	}

	// Extract and display the news articles
	articles := data["articles"].([]interface{})
	for _, article := range articles {
		articleMap := article.(map[string]interface{})
		title := articleMap["title"].(string)
		source := articleMap["source"].(map[string]interface{})["name"].(string)
		fmt.Printf("%s - %s\n", title, source)
	}
}
