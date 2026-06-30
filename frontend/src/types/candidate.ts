export interface Experience{

    company?:string;

    title?:string;

}

export interface Education{

    degree?:string;

    institution?:string;

}

export interface Personal{

    full_name?:string;

    emails:string[];

    phones:string[];

    location?:string;

}

export interface Professional{

    headline?:string;

    years_experience?:number;

    skills:string[];

    experience:Experience[];

}

export interface Candidate{

    candidate_id:string;

    personal:Personal;

    professional:Professional;

    education:Education[];

    links:string[];

    provenance:any[];

    metadata:{

        confidence:number;

        sources:string[];

    }

}