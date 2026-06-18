resource "aws_ecr_repository" "fintech_ledger_repo" {
  name                 = "fintech-ledger-app"
  force_delete         = true
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}