# Makefile for CloudShop CLI App (Python)

APP=cloudshop.py
DB=cloudshop.db

.PHONY: all build run clean

all: build

build:
	chmod +x build.sh
	chmod +x run.sh
	@echo "✅ Build complete. Use 'make run' to start."

run:
	./run.sh
	@echo "✅ Start running!!"

clean:
	@echo "🧹 Removing database..."
	@rm -f $(DB)
	@echo "✅ Clean complete."