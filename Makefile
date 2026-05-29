servicesUp:
	docker compose -f "infra/compose.yaml" up -d

servicesStop:
	docker compose -f "infra/compose.yaml" stop

servicesDown:
	docker compose -f "infra/compose.yaml" down