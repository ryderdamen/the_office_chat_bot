IMAGE_NAME = gcr.io/radical-sloth/the-office-chat-bot

.PHONY: build
build:
	@echo "Building latest image"; \
	docker build -t $(IMAGE_NAME) .

.PHONY: run
run:
	@docker run -p 5000:5000 $(IMAGE_NAME)

.PHONY: push
push:
	@docker push $(IMAGE_NAME)

.PHONY: deploy
deploy:
	@kubectl apply -f kubernetes/deployment.yaml -f kubernetes/service.yaml -f kubernetes/hpa.yaml
