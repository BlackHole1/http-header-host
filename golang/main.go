package main

import (
	"fmt"
	"log"
	"net/http"
)

type Data struct {
  status bool
  header http.Header
}

func handle(w http.ResponseWriter, r *http.Request) {
  data := Data{
    status: true,
    header: r.Header,
  }
  fmt.Fprintf(w, "%v", data);
}

func main() {
  http.HandleFunc("/", handle);
  log.Fatal(http.ListenAndServe(":8083", nil));
}
