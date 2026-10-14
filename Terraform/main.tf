provider "http" {
}

data "http" "api_url" {
  url = "${var.base}${var.subnet}/${var.mask}"
  method = "GET"
}
