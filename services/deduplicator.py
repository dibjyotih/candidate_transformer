from typing import List

from models.candidate import Candidate


class Deduplicator:

    @staticmethod
    def merge(candidates: List[Candidate]):

        merged = {}

        for candidate in candidates:

            if candidate.emails:

                key = candidate.emails[0]

            elif candidate.phones:

                key = candidate.phones[0]

            else:

                key = candidate.full_name.lower()

            if key not in merged:

                merged[key] = candidate

            else:

                existing = merged[key]

                existing.skills = list(
                    set(existing.skills + candidate.skills)
                )

                existing.links = list(
                    set(existing.links + candidate.links)
                )

                existing.emails = list(
                    set(existing.emails + candidate.emails)
                )

                existing.phones = list(
                    set(existing.phones + candidate.phones)
                )

                existing.experience.extend(candidate.experience)

                existing.education.extend(candidate.education)

                existing.provenance.extend(candidate.provenance)

                existing.confidence.extend(candidate.confidence)

        return list(merged.values())