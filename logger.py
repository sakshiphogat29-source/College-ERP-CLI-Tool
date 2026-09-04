import logging
from pathlib import Path

log_folder = Path("__file__").parent / "logs"
log_folder.mkdir(exist_ok=True,parents=True)

logging.basicConfig(
    filename=log_folder / "erp.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

logger = logging.getLogger(__name__)