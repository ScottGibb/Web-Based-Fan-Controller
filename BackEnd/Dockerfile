
# A Simple Dockerfile for hosting the backend of the PythonWebApp

FROM debian:trixie-slim

# Set the working directory to /app
WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends python3 python3-lgpio ca-certificates curl && \
    rm -rf /var/lib/apt/lists/*

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin:${PATH}"

COPY pyproject.toml /app/
RUN uv sync --system --no-install-project


# Copy the current directory contents into the container at /app
COPY src /app

RUN uv sync --system

EXPOSE 5000

ENV MOCK=""
# Run app.py when the container launches
CMD ["sh", "-c", "uv run --system python app.py $MOCK"]
