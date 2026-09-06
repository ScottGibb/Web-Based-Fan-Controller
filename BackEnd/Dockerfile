
# A Simple Dockerfile for hosting the backend of the PythonWebApp

FROM debian:trixie-slim

# Set the working directory to /app
WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        python3 \
        ca-certificates \
        gpg \
        curl && \
    curl -fsSL https://archive.raspberrypi.com/debian/raspberrypi.gpg.key | \
        gpg --dearmor -o /usr/share/keyrings/raspberrypi-archive-keyring.gpg && \
    printf '%s\n' \
        'deb [arch=arm64 signed-by=/usr/share/keyrings/raspberrypi-archive-keyring.gpg] https://archive.raspberrypi.com/debian/ trixie main' \
        > /etc/apt/sources.list.d/raspberrypi.list && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends python3-lgpio && \
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
