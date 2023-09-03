# Run

## Localhost

```bash
python run.py

uvicorn app:app --reload --port 8000
```

## Start system

```bash
cd /home/pi/polarease-raspberry-pi/ && source .venv/bin/activate && python3 /home/pi/polarease-raspberry-pi/ uvicorn app:app --reload --port 8000 &
```