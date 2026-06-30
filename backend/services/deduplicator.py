from typing import List
from rapidfuzz import fuzz

from models.candidate import Candidate


class Deduplicator:

    NAME_THRESHOLD = 85

    @staticmethod
    def merge(candidates: List[Candidate]) -> List[Candidate]:

        merged = []

        for candidate in candidates:

            existing = Deduplicator.find_match(candidate, merged)

            if existing:

                Deduplicator.merge_candidate(existing, candidate)

            else:

                merged.append(candidate)

        return merged

    @staticmethod
    def find_match(candidate: Candidate,
                   merged: List[Candidate]):

        for existing in merged:

            # -------------------------
            # Email Match
            # -------------------------

            if (
                set(candidate.personal.emails)
                &
                set(existing.personal.emails)
            ):
                return existing

            # -------------------------
            # Phone Match
            # -------------------------

            if (
                set(candidate.personal.phones)
                &
                set(existing.personal.phones)
            ):
                return existing

            # -------------------------
            # Name Similarity
            # -------------------------

            if (
                candidate.personal.full_name
                and
                existing.personal.full_name
            ):

                score = fuzz.token_sort_ratio(

                    candidate.personal.full_name.lower(),

                    existing.personal.full_name.lower()

                )

                if score >= Deduplicator.NAME_THRESHOLD:

                    return existing

        return None

    @staticmethod
    def merge_candidate(existing: Candidate,
                        new: Candidate):

        # -------------------------
        # Personal
        # -------------------------

        existing.personal.emails = sorted(
            list(
                set(
                    existing.personal.emails
                    +
                    new.personal.emails
                )
            )
        )

        existing.personal.phones = sorted(
            list(
                set(
                    existing.personal.phones
                    +
                    new.personal.phones
                )
            )
        )

        if (
            not existing.personal.location
            and
            new.personal.location
        ):
            existing.personal.location = new.personal.location

        # Better name (longer wins)

        if (
            new.personal.full_name
            and
            (
                not existing.personal.full_name
                or
                len(new.personal.full_name)
                >
                len(existing.personal.full_name)
            )
        ):
            existing.personal.full_name = new.personal.full_name

        # -------------------------
        # Professional
        # -------------------------

        existing.professional.skills = sorted(
            list(
                set(
                    existing.professional.skills
                    +
                    new.professional.skills
                )
            )
        )

        existing.professional.experience.extend(
            new.professional.experience
        )

        if (
            not existing.professional.headline
            and
            new.professional.headline
        ):
            existing.professional.headline = (
                new.professional.headline
            )

        if (
            new.professional.years_experience
            and
            (
                existing.professional.years_experience is None
                or
                new.professional.years_experience
                >
                existing.professional.years_experience
            )
        ):

            existing.professional.years_experience = (
                new.professional.years_experience
            )

        # -------------------------
        # Education
        # -------------------------

        existing.education.extend(new.education)

        # -------------------------
        # Links
        # -------------------------

        existing.links = sorted(
            list(
                set(
                    existing.links
                    +
                    new.links
                )
            )
        )

        # -------------------------
        # Metadata
        # -------------------------

        existing.metadata.sources = sorted(
            list(
                set(
                    existing.metadata.sources
                    +
                    new.metadata.sources
                )
            )
        )

        # -------------------------
        # Provenance
        # -------------------------

        existing.provenance.extend(new.provenance)