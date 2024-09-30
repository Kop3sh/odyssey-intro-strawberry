import strawberry


@strawberry.type(description="A single audio file, usually a song")
class Track:
    id: strawberry.ID
    name: str
    duration_ms: int
    explicit: bool
    uri: str
