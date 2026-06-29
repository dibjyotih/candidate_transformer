from models.candidate import Candidate


class ConflictResolver:

    @staticmethod
    def resolve(candidate: Candidate):

        if not candidate.full_name:

            candidate.full_name = "Unknown"

        if not candidate.headline and candidate.experience:

            candidate.headline = candidate.experience[-1].title

        candidate.skills = sorted(list(set(candidate.skills)))

        return candidate