package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"net/url"
	"os"
	"time"

	"github.com/joho/godotenv"
	"github.com/tidwall/gjson"
)

func main() {
	// Load environment variables from .env file
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}

	// Get the API key from the environment variables
	apiKey := os.Getenv("NEWS_API_KEY")

	// Calculate the date range for the past week
	now := time.Now()
	weekAgo := now.AddDate(0, 0, -7)
	from := weekAgo.Format("2006-01-02")
	to := now.Format("2006-01-02")

	// Make the API request
	u, err := url.Parse("https://newsapi.org/v2/top-headlines")
	if err != nil {
		log.Fatal("Error parsing the URL")
	}

	params := url.Values{
		"country": {"us"},
		"apiKey":  {apiKey},
		"from":    {from},
		"to":      {to},
	}
	u.RawQuery = params.Encode()

	resp, err := http.Get(u.String())
	if err != nil {
		log.Fatal("Error making the request:", err)
	}
	defer resp.Body.Close()

	// Check if the request was successful
	if resp.StatusCode != http.StatusOK {
		log.Fatal("Error:", resp.Status)
	}

	resContent, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Fatal("Error reading the body:", err)
	}

	value := gjson.GetBytes(resContent, "articles.#.content")
	value.ForEach(func(key, value gjson.Result) bool {
		fmt.Println(value)
		fmt.Println("------")
		return true
	})
}
