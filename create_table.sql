CREATE TABLE stages (  
      id NUMBER PRIMARY KEY  
    , organization_id NUMBER  
    , name VARCHAR(1024)  
    , order NUMBER  
    , active BOOLEAN  
    , created_at TIMESTAMP  
    , updated_at TIMESTAMP  
);  

CREATE TABLE application_stages (  
      application_id NUMBER  
    , stage_id NUMBER  
    , entered_on TIMESTAMP  
    , exited_on TIMESTAMP  
    , stage_name VARCHAR(16777216)  
    , organization_id NUMBER  
    , PRIMARY KEY (application_id, stage_id)  
    , FOREIGN KEY (stage_id) REFERENCES stages(id)  
    , FOREIGN KEY (organization_id) REFERENCES stages(organization_id)  
);  