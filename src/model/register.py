from dataclasses import dataclass


@dataclass
class Register:
    name: str
    document_number: str
    register_date: str
    liveness: str
    identity_match: str
    face_scan: str
    face_crop: str
    doc_front_scan_crop: str
    doc_back_scan_crop: str


