
# A Simple Dockerfile for hosting the backend of the PythonWebApp

FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim

# Set the working directory to /app
WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        python3 \
        ca-certificates \
        curl && \
    curl -fsSL -o /tmp/liblgpio1.deb \
        https://archive.raspberrypi.com/debian/pool/main/l/lg-gpio/liblgpio1_0.2.2-1~rpt1+trixie_arm64.deb && \
    curl -fsSL -o /tmp/python3-lgpio.deb \
        https://archive.raspberrypi.com/debian/pool/main/l/lg-gpio/python3-lgpio_0.2.2-1~rpt1+trixie_arm64.deb && \
    dpkg -i /tmp/liblgpio1.deb /tmp/python3-lgpio.deb && \
    rm -rf /tmp/liblgpio1.deb /tmp/python3-lgpio.deb /var/lib/apt/lists/*

ENV PYTHONPATH="/usr/lib/python3/dist-packages"
RUN python -c "import lgpio; print(lgpio.__file__)"

COPY pyproject.toml /app/
RUN uv lock && uv sync --no-install-project


# Copy the current directory contents into the container at /app
COPY src /app

RUN uv sync

EXPOSE 5000

ENV MOCK=""
# Run app.py when the container launches
CMD ["sh", "-c", "uv run python app.py $MOCK"]
