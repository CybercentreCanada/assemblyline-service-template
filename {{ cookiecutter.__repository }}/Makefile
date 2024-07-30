ifndef VERSION
$(error VERSION is undefined)
endif

TAG?=latest
ORG?={{ cookiecutter.org_name_short }}

ifneq ($(ORG)x, x)
ORG:=$(ORG)/
endif
ifneq ($(REGISTRY)x, x)
ORG:=$(REGISTRY)/
endif

.PHONY: default
default: build

.PHONY: build
build:
	docker build \
		--pull \
		--build-arg version=$(VERSION) \
		--build-arg branch=$(TAG) \
		-t $(REGISTRY)$(ORG){{ cookiecutter.__repository }}:$(TAG)\
		-f ./Dockerfile \
		.
