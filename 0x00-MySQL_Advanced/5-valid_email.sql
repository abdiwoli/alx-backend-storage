CREATE TRIGGER valid_email_triger 
BEFORE UPDATE on users.email
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN SET NEW.valid_email = 0;
  END IF;
END;
