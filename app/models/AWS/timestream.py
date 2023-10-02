class TimeStream:
    def create_table(self, HT_TTL_HOURS, CT_TTL_DAYS, DATABASE_NAME, TABLE_NAME):
        print("Creating table")
        retention_properties = {
            'MemoryStoreRetentionPeriodInHours': HT_TTL_HOURS,
            'MagneticStoreRetentionPeriodInDays': CT_TTL_DAYS
        }
        try:
            self.client.create_table(DatabaseName=DATABASE_NAME, TableName=TABLE_NAME, RetentionProperties=retention_properties)
            print("Table [%s] successfully created." % TABLE_NAME)
        except self.client.exceptions.ConflictException:
            print("Table [%s] exists on database [%s]. Skipping table creation" % (
                TABLE_NAME, DATABASE_NAME))
        except Exception as err:
            print("Create table failed:", err)